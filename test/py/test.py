#!/usr/bin/env python3

import hashlib
from google.protobuf.json_format import MessageToJson
from google.protobuf.text_format import MessageToString
import ssb_birch_pb2 as SSB

# build a log entry
# a) backlink (demoes two hash values)
hr1 = SSB.HashRef(hashType = SSB.HT_SHA256,
                 hashValue = b'\xde\xad\xbe\xef')
hr2 = SSB.HashRef(hashType = SSB.HT_SHA512224,
                 hashValue = b'\xaa\xbb\xcc\xef')
bl  = [hr1, hr2]

# b) prepare contents (two pieces, one is in-event, the other is off-chain)
lc1 = SSB.LogContent(data = b'\x11\x22\x33\x44')
attch = b'\x99\x88\x77\x66'
lc2 = SSB.LogContent(dptr = SSB.inChainPtr(size=len(attch), attachNo = 1))

# c) signature algo
si = SSB.SignatureInfo(sigType = SSB.ST_SHA256_WITH_ED25519)
                      # keyLocator = SSB.KeyLocator(value = b'keyloc'))


# d) the log entry's event record
hr = SSB.HashRef(hashType = SSB.HT_SHA256,
                 hashValue = hashlib.sha256(attch).digest())
ae = SSB.AttachEntry(size = len(attch),
                     hashRefs = [ hr ])
le = SSB.LogEvent(contents = [lc1, lc2],
                  backLink = bl,
                  sigInfo = si,
                  attachDir = [ae])

# e) compute signature (SSB.SHA256_WITH_EC25519):
ser = le.SerializeToString()
dig = hashlib.sha256(ser).digest()
sig = dig # here we would encrypt the digest with the private key

# f) final assembly
sle = SSB.LogEntry(event = le, sigValue = sig, attachments = [ attch ])

# create a log object, for pretty printing only:
fid = SSB.FeedID(feedType = SSB.FT_SSB_ED25519, feedValue= b'ID_in_32bytes')
log = SSB.Log(feedID = fid, log = [sle])

print("** Example protobuf log, pretty-printed as text:\n")
print(MessageToString(log))
print("** Example protobuf log, this time with field numbers:\n")
print(MessageToString(log, use_field_number=True))
print(f"** serialized, the above log protobuf is {len(log.SerializeToString())} bytes long,")
print(f"   the event itself has {len(le.SerializeToString())} bytes\n\n---\n")

print("** Example protobuf log, as JSON: log object = ")
print(MessageToJson(log)) # , including_default_value_fields=True))

# eof
