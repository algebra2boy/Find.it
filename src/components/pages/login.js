import {React, useState, useRef, useEffect} from 'react';
import { useNavigate } from 'react-router-dom';
import "../LogIn.css";
import NavigationBar from '../NavigationBar';
import axios from 'axios';

export function LogIn(){
    const userRef = useRef();
    const errRef = useRef();

    const [user, setUser] = useState('');
    const [pass, setPass] = useState('');
    const [errMsg, setErrMsg] = useState('');


    const navigate = useNavigate();

    useEffect(() => {
        userRef.current.focus();
    }, [])

    useEffect(() => {
        setErrMsg('');
    }, [user, pass])

    // direct to dashboard
    const handleSubmit = async (e) => {
        axios.post('http://localhost:5000/login', {
            password: pass,
            email: user,
          })
          .then(function (response) {
            navigate('/dashboard', {state:{response}});
          })
          .catch(function (error) {
            console.log(error);
          });
    }

    return (
        <>
        <NavigationBar />
        <div className='login-container'>
        <section>
            <p ref={errRef} className={errMsg ? "errmsg" : "offscreen"} aria-live="assertive">{errMsg}</p>
                <form onSubmit={handleSubmit}>
                    <h4>Log in to your account</h4>
                    <input
                        type="email"
                        id="userName"
                        ref={userRef}
                        onChange={(e) => setUser(e.target.value)}
                        value={user}
                        autoComplete="off"
                        placeholder={"Username"}
                        required
                    />
                    <input
                        type="password"
                        id="password"
                        ref={userRef}
                        onChange={(e) => setPass(e.target.value)}
                        value={pass}
                        placeholder={"Password"}
                        required
                    />
                    <button className='sign-button'>Log In</button>
                </form>
        </section>
        </div>
        </>
    )
}
export default LogIn;