import './App.css';
import React from 'react';
import NavigationBar from './components/NavigationBar';
import { BrowserRouter as Router, Routes, Route} from "react-router-dom"; // activate and direct to different link
import './App.css';

function App() {
  return (
    <>
    <Router>
      <NavigationBar />
    </Router>
    </>

  );
}

export default App;
