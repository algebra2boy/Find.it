import {React, useState, useRef, useEffect} from 'react';
import NavigationBar from '../NavigationBar';
import "../LogIn.css";

export function SignUp() {
    const userRef = useRef();
    const errRef = useRef();

    const [user, setUser] = useState('');
    const [pass, setPass] = useState('');
    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    const [phone, setPhone] = useState('');
    const [errMsg, setErrMsg] = useState('');
    const [success, setSucess] = useState(false);

    useEffect(() => {
        userRef.current.focus();
    }, [])

    useEffect(() => {
        setErrMsg('');
    }, [user, pass])

    return (
        <>
        <NavigationBar/>
        <div className='login-container'>
            <section>
                <p ref={errRef} className={errMsg ? "errmsg" : "offscreen"} aria-live="assertive">{errMsg}</p>
                <form>
                    <h4>Create your account</h4>
                    <input
                        type="email"
                        id="userName"
                        ref={userRef}
                        onChange={(e) => setUser(e.target.value)}
                        value={user}
                        autoComplete="off"
                        placeholder={"email"}
                        required
                    />
                    <input
                        type="text"
                        id="password"
                        ref={userRef}
                        onChange={(e) => setPass(e.target.value)}
                        value={pass}
                        autoComplete="off"
                        placeholder={"password"}
                        required
                    />
                    <input
                        type="text"
                        id="firstName"
                        ref={userRef}
                        onChange={(e) => setFirstName(e.target.value)}
                        value={firstName}
                        autoComplete="off"
                        placeholder={"first name"}
                        required
                    />
                    <input
                        type="text"
                        id="lastName"
                        ref={userRef}
                        onChange={(e) => setLastName(e.target.value)}
                        value={lastName}
                        autoComplete="off"
                        placeholder={"last name"}
                        required
                    />
                    <input
                        type="text"
                        id="phone"
                        ref={userRef}
                        onChange={(e) => setPhone(e.target.value)}
                        value={phone}
                        autoComplete="off"
                        placeholder={"phone number"}
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