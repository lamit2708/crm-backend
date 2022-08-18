# Complete guideline of Redux
[REF](https://www.valentinog.com/blog/redux/)
## Using Redux Dev Tool

[REF](https://github.com/valentinogagliardi/react-redux-tutorial/blob/your-first-redux-middleware/src/js/store/index.js)

```Python
// src/js/store/index.js
import { createStore, applyMiddleware, compose } from "redux";
import rootReducer from "../reducers/index";
import { forbiddenWordsMiddleware } from "../middleware";

const storeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;

const store = createStore(
  rootReducer,
  storeEnhancers(applyMiddleware(forbiddenWordsMiddleware))
);

export default store;
```
