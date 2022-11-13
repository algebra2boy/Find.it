import {React, useState, useRef, useEffect} from 'react';
import NavigationBar from '../NavigationBar';
import "../LogIn.css";
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

export function SignUp() {
    const userRef = useRef();
    const errRef = useRef();
    const navigate = useNavigate();

    const [user, setUser] = useState('');
    const [pass, setPass] = useState('');
    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    const [phone, setPhone] = useState('');
    const [errMsg, setErrMsg] = useState('');

    useEffect(() => {
        userRef.current.focus();
    }, [])

    useEffect(() => {
        setErrMsg('');
    }, [user, pass])

    const handleSubmit = async () => {
        axios.post('http://localhost:5000/signup', {
            firstName: firstName,
            lastName: lastName,
            phone: phone,
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
        <NavigationBar/>
        <div className='login-container'>
            <section>
                <p ref={errRef} className={errMsg ? "errmsg" : "offscreen"} aria-live="assertive">{errMsg}</p>
                <form onSubmit={handleSubmit}>
                    <h4>Create your account</h4>
                    <input
                        type="email"
                        id="userName"
                        ref={userRef}
                        onChange={(e) => setUser(e.target.value)}
                        value={user}
                        autoComplete="off"
                        placeholder={"Email"}
                        required
                    />
                    <input
                        type="text"
                        id="password"
                        ref={userRef}
                        onChange={(e) => setPass(e.target.value)}
                        value={pass}
                        autoComplete="off"
                        placeholder={"Password"}
                        required
                    />
                    <input
                        type="text"
                        id="firstName"
                        ref={userRef}
                        onChange={(e) => setFirstName(e.target.value)}
                        value={firstName}
                        autoComplete="off"
                        placeholder={"First Name"}
                        required
                    />
                    <input
                        type="text"
                        id="lastName"
                        ref={userRef}
                        onChange={(e) => setLastName(e.target.value)}
                        value={lastName}
                        autoComplete="off"
                        placeholder={"Last Name"}
                        required
                    />
                    <input
                        type="text"
                        id="phone"
                        ref={userRef}
                        onChange={(e) => setPhone(e.target.value)}
                        value={phone}
                        autoComplete="off"
                        placeholder={"Phone Number"}
                        required
                    />
                <button className='sign-button'>Sign Up</button>
            </form>
        </section>
        </div>
        </>
    )
}

export default SignUp;