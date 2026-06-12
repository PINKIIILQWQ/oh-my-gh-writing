# 03 Enhancement 测试

## Enhancement: Allow `res.send()` to accept streaming bodies

## Current Limitation

Express `res.send()` is designed around sending a complete response body. In the prompt's target case, that means callers must prepare the full payload before sending it.

For large files or generated responses, this can force unnecessary buffering in application memory.

## Proposed Improvement

Allow `res.send()` to accept a `ReadableStream` body and stream it to the HTTP response without loading the full payload first.

Example draft API:

```js
app.get("/download", async (req, res) => {
  const stream = await createLargeFileStream()

  res.type("application/octet-stream")
  return res.send(stream)
})
```

Expected behavior:

- `ReadableStream` chunks are written to the response as they become available.
- Backpressure is respected.
- Stream errors are surfaced through Express error handling when possible.
- Existing `string`, `Buffer`, object, and JSON response behavior remains unchanged.

## Before / After

### Before

```js
app.get("/download", async (req, res) => {
  const file = await fs.promises.readFile("large-export.zip")
  res.type("application/zip")
  res.send(file)
})
```

### After

```js
app.get("/download", (req, res) => {
  const file = fs.createReadStream("large-export.zip")
  res.type("application/zip")
  res.send(file)
})
```

## Compatibility

This should be additive if stream detection is strict and does not change how existing supported body types are interpreted.

Compatibility concerns to confirm:

- How `ReadableStream` should interact with `Content-Length`.
- Whether Node.js `Readable` and Web `ReadableStream` should both be supported.
- Whether `res.send(stream)` should implicitly call `stream.pipe(res)` or use a shared internal response helper.
- How headers behave if the stream errors after the first chunk has been sent.

## Verification to Run

- Unit: existing `res.send()` body types still produce the same response.
- Unit: `ReadableStream` response streams multiple chunks in order.
- Unit: stream errors before headers are sent reach Express error middleware.
- Integration: large file streaming does not require preloading the full file into memory.
- Compatibility: confirm behavior for Node.js `Readable` and Web `ReadableStream`, or document which one is supported first.
