# Integrate AdminLTE into reactjs

[REF](https://github.com/erdkse/adminlte-3-react)

## Add sass

[sass](https://blog.bitsrc.io/how-to-use-sass-and-css-modules-with-create-react-app-83fa8b805e5e)

## Add AdminLTE

```bash
yarn add admin-lte@v3 bootstrap
```

## Import AdminLTE css

```bash
mkdir static
mkdir styles
cat <<'-EOF' > styles/styles.scss
/**
 * App entry scss file using bootstrap and AdminLTE v2
 *
 * @url https://getbootstrap.com/docs/4.0/getting-started/theming/
 * @url https://getbootstrap.com/docs/4.0/getting-started/webpack/#importing-precompiled-sass
 */
@import '~bootstrap/scss/bootstrap';
@import "~admin-lte/build/scss/AdminLTE-raw.scss";

$color: blue;
h1 {
  color: $color;
}
-EOF
```

## Copy AdminLTE JS

cp node_modules/admin-lte/dist/js/adminlte.js static/
cp node_modules/admin-lte/dist/js/adminlte.js.map static/
cp node_modules/admin-lte/dist/js/adminlte.min.js static/
cp node_modules/admin-lte/dist/js/adminlte.min.js.map static/

## Create main page to include AdminLTE js

```bash
cat <<'-EOF' > pages/_document.js
import Document, {Head, Main, NextScript} from 'next/document'

export default class MyDocument extends Document {
    render() {
        return (
            <html>
            <Head>
                <title>My Next.js Project</title>
                <link rel="stylesheet" href="/_next/static/style.css"/>
                <link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet"/>
                <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js"/>
                <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"/>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js"/>
                {/* This provides all admin-lte functionality - we copied the files to our static directory above */}
                <script src="/static/adminlte.js"/>
            </Head>
            <body className="sidebar-mini">
            <Main/>
            <NextScript/>
            </body>
            </html>
        )
    }
}
-EOF
```

## Create Layout

```bash
mkdir -p components/Layout
```

- AdminContent.js
- AdminControlSidebar.js
- AdminFooter.js
- AdminHeader.js
- AdminLayoutHoc.js
- AdminSidebar.js
