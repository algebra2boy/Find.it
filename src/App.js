import './App.css';
import React from 'react';
import { BrowserRouter as Router, Routes, Route} from "react-router-dom"; // activate and direct to different link
import './App.css';
import Home from "./components/pages/home";
import LogIn from './components/pages/login';
import { SignUp } from './components/pages/SignUp';
import {MainPage} from './components/pages/MainPage';

function App() {
  return (
    <>
    <Router>
      <Routes>
        <Route path = '/' element={<Home />} />
        <Route path = 'login' element={<LogIn />} />
        <Route path = 'sign-up' element={<SignUp />} />
        <Route path = 'dashboard' element={<MainPage />} />
      </Routes>
    </Router>
    </>

  );
}

export default App;
