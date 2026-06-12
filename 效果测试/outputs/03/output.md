### Enhancement: Accept ReadableStream in res.send()

**Current limitation**
Express 4.x `res.send()` detects body type via `instanceof` checks for `string`, `Buffer`, and `Object`. When passed a Web API `ReadableStream`, none of these match and the stream is serialized as `[object ReadableStream]`.

**Proposed behavior**
Detect `ReadableStream` and pipe it directly to the response without buffering the entire body into memory.

**Before**
```js
// Must buffer entire stream first
const chunks = [];
for await (const chunk of readableStream) {
  chunks.push(chunk);
}
res.send(Buffer.concat(chunks));
```

**After**
```js
// Stream directly — no buffering
res.send(readableStream);
```

**Compatibility**
Additive change. `res.send()` signature extended with one additional type check. Existing usage unaffected. Requires Node.js 18+ for `ReadableStream` global.

**Verification (to run)**
- Unit: res.send(new ReadableStream(...)) produces chunked transfer response
- Memory: 500MB file should not spike heap beyond 10MB
- Edge: null body, already-ended response, aborted stream
