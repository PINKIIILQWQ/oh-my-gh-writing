---
scenario: Enhancement
mode: concise
case-sources: https://github.com/django/django
input-prompt: ../../prompts/03-enhancement.md
---

### Enhancement: ReadableStream support in res.send()

**Current limitation**
res.send() cannot accept Web ReadableStream - users must buffer entire stream
into memory first, defeating the purpose of streaming.

**Before**
```js
const arr = []; for await (const chunk of readableStream) arr.push(chunk);
res.send(Buffer.concat(arr));
```

**After**
```js
res.send(readableStream);
// Streams directly to response without buffering
```

**Compatibility**
Additive change - only new ReadableStream detection added.
