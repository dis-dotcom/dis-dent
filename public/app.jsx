'use strict';

const e = React.createElement;

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {

    }
  }

  render() {
    return (
        <p>App</p>
    );
  }
}

ReactDOM.createRoot(document.querySelector('#root'))
        .render(React.createElement(App));
