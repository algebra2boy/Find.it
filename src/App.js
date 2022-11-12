import './App.css';
import React from 'react';
import NavigationBar from './components/NavigationBar';
import { BrowserRouter as Router, Routes, Route} from "react-router-dom"; // activate and direct to different link
import './App.css';
import Home from "./components/pages/home";

function App() {
  return (
    <>
    <Router>
      <NavigationBar />
      <Home/>
      <Routes>
        <Route path = '/' exact component={Home} />
      </Routes>
    </Router>
    </>

  );
}

export default App;
