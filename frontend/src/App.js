import "./App.css";
import React, { useState, useEffect } from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";

function App() {
  return (
    <Router>
      <Switch>
        <Route exact path="/">
          <Home />
        </Route>
        <Route path="/restaurants">
          <Restaurants />
        </Route>
      </Switch>
    </Router>
  );
}

function Home() {
  const [state, setState] = useState("");

  useEffect(() => {
    fetch("http://localhost:5000")
      .then((res) => res.text())
      .then(
        (res) => {
          setState(res);
        },
        (error) => {
          console.log(error);
        }
      );
  }, []);

  return <div>{state}</div>;
}

function Restaurants() {
  const [state, setState] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5000/restaurants")
      .then((res) => res.json())
      .then(
        (res) => {
          setState(res);
        },
        (error) => {
          console.log(error);
        }
      );
  }, []);

  return (
    <div class="App">
      {state.map((data) => (
        <li>
          {data.name} - {data.score}
        </li>
      ))}
    </div>
  );
}

export default App;
