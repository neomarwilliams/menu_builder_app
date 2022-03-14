import './App.css';
import React from 'react';
import axios from 'axios';

class App extends React.Component {

  state = {
    details : [],
  }

  componentDidMount() {

    let data;
    axios.get('http://localhost:8000/wel/')
    .then (res => {
      data = res.data;
      this.setState({
        details:data
      });
    })
    .catch(err => {})
  }
  render() {
    return (
      <div className="App">
        {this.state.details.map((detail,id) =>(
          <div key={id}>
            <div>
              <div>
                <h1>{detail.detail}</h1>
                <footer>--- by
                  <cite title='Source Title'>{detail.name}</cite>
                </footer>
              </div>
            </div>  
          </div>

        ))}
      </div>
    );
  }
}

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

export default App;
