# Integrate AdminLTE into reactjs

[REF](https://github.com/erdkse/adminlte-3-react)

## Add sass

[sass](https://blog.bitsrc.io/how-to-use-sass-and-css-modules-with-create-react-app-83fa8b805e5e)

## Install AdminLTE

```bash
yarn add admin-lte@v3 bootstrap
```

## Change file .css into s.css

src/index.css => src/index.scss
src/App.css => src/App.scss

## Update import file css

App.js>import "./App.scss";
Index.js> import "./index.scss";

## Import CSS link

Copy css link from AdminLTE/index3.html into yourproject/index.scss
[REF](https://create-react-app.dev/docs/adding-a-sass-stylesheet/)

```scss
@import "http://code.ionicframework.com/ionicons/2.0.1/css/ionicons.min.css";

@import "https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,400i,700";

@import "~admin-lte/plugins/fontawesome-free/css/all.min.css";

@import "~admin-lte/dist/css/adminlte.min.css";
```

## Import JS

```jsx
  <script src="%PUBLIC_URL%/plugins/jquery/jquery.min.js"></script>
  <!-- Bootstrap -->
  <script src="%PUBLIC_URL%/plugins/bootstrap/js/bootstrap.bundle.min.js"></script>
  <!-- AdminLTE -->
  <script src="%PUBLIC_URL%/dist/js/adminlte.js"></script>

  <!-- OPTIONAL SCRIPTS -->
  <script src="%PUBLIC_URL%/plugins/chart.js/Chart.min.js"></script>
  <script src="%PUBLIC_URL%/dist/js/demo.js"></script>
  <script src="%PUBLIC_URL%/dist/js/pages/dashboard3.js"></script>
```
