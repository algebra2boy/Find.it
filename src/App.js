import './App.css';
import React from 'react';
import { BrowserRouter as Router, Routes, Route} from "react-router-dom"; // activate and direct to different link
import './App.css';
import Home from "./components/pages/home"
import LogIn from './components/pages/LogIn';

function App() {
  return (
    <>
    <Router>
      <Routes>
        <Route path = '/' element={<Home />} />
        <Route path = 'login' element={<LogIn />} />
      </Routes>
    </Router>
    </>

  );
}

export default App;
