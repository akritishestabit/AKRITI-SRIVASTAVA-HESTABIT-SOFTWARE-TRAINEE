const { AsyncLocalStorage } = require("async_hooks");

const asyncLocalStorage = new AsyncLocalStorage();

function runWithContext(req, res, next) {
  asyncLocalStorage.run(
    { requestId: req.requestId },
    () => next()
  );
}

function getRequestId() {
  const store = asyncLocalStorage.getStore();
  return store ? store.requestId : null;
}

module.exports = {
  runWithContext,
  getRequestId,
};