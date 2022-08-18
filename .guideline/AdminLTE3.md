# Integrate AdminLTE3 into the frontend Reactjs

[Reference](https://www.youtube.com/watch?v=LFVMs_jmhNU)

## Install packages

```bash
npm install admin-lte@^3.0 --save
```

## Download Adminlte3

[adminlte3](https://github.com/ColorlibHQ/AdminLTE/archive/v3.0.5.zip)

## Import plugins

Copy folder dist, plugins into your project

AdminLTE/dist to yourproject/public/dist
AdminLTE/plugins to yourproject/public/plugins

## Import CSS link

Copy css link from AdminLTE/index3.html into yourproject/public/index.html

Add %PUBLIC_URL%/ into your link to access folder plugins, dist
Add the follow code into the tag head

```HTML

 <link rel="stylesheet" href="%PUBLIC_URL%/plugins/fontawesome-free/css/all.min.css">
  <!-- IonIcons -->
  <link rel="stylesheet" href="http://code.ionicframework.com/ionicons/2.0.1/css/ionicons.min.css">
  <!-- Theme style -->
  <link rel="stylesheet" href="%PUBLIC_URL%/dist/css/adminlte.min.css">
  <!-- Google Font: Source Sans Pro -->
  <link href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,400i,700" rel="stylesheet">
```

## Import JS link

Copy js link from AdminLTE/index3.html into yourproject/public/index.html

Add %PUBLIC_URL%/ to access folder dist, plugins
Add the follow code into the end of tag body

```HTML
 <!-- jQuery -->
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

## Add class into the tag body

Reference the classes of the tag body from AdminLTE/index3.html and add to yourproject/public/index.html

```HTML
 <body class="hold-transition sidebar-mini" >
```

## Add the tag div.wrapper

Add the tag div.wrapper into App.js

```jsx
function App() {
  return <div className="wrapper"></div>;
}
```

## Add Components

Create folder src/components
Then add the following components:

1. Header:
2. Menu
3. Footer
4. Content

## Demo create the components Footer

Create the file src/components/Footer.js
Type rfc, and press TAB to generate the component

```jsx
import React from "react";

export default function Footer() {
  return <div></div>;
}
```

Copy the block of Main Footer and replace the tag div
Use the extension HTML TO JSX to convert the code that you just past.

And the result

```jsx
import React from "react";

export default function Footer() {
  return (
    <footer className="main-footer">
      <strong>
        Copyright © 2014-2019 <a href="http://adminlte.io">AdminLTE.io</a>.
      </strong>
      All rights reserved.
      <div className="float-right d-none d-sm-inline-block">
        <b>Version</b> 3.0.5
      </div>
    </footer>
  );
}
```

## Convert the blocks into the components

Convert the following blocks of code from AdminLTE/index3.html into the components

Use the extension HTML TO JSX to convert.

- Navbar => Components Header

- Main Sidebar Container => Components Menu

- Content Wrapper => Components Content

- Main Footer => Components Footer

## Import Components into App.js

```jsx
import React from "react";
import Content from "./components/Content";
import Footer from "./components/Footer";
import Header from "./components/Header";
import Menu from "./components/Menu";

export default function App() {
  return (
    <div className="wrapper">
      <Header />
      <Menu />
      <Content />
      <Footer />
    </div>
  );
}
```
