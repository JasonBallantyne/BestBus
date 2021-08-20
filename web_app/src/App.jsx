import './App.css';
import React, { Component } from 'react';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Redirect
} from "react-router-dom";
import EnglishApp from './english-language/EnglishApp';
import GaeilgeApp from './gaeilge-language/GaeilgeApp';
import 'bootstrap/dist/css/bootstrap.min.css';

let language = null;
class App extends Component {
  constructor(props) {
    super(props)
    this.state = { matches: window.matchMedia("(min-width: 1000px)").matches };
  };
  componentWillMount() {
   language = localStorage.getItem('language') || '/en-ie'
  };
  render() {
    return (
      <Router>
        <Switch>
          <Route exact path="/">
            <Redirect to={language} />
          </Route>
          <Route path="/en-ie">
            <EnglishApp passedState={this.state}/>
          </Route>
          <Route path="/ga-ie">
            <GaeilgeApp passedState={this.state}/>
          </Route>
        </Switch>
      </Router>
    );
  }
}

export default App;