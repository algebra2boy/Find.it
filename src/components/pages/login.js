import {React, useState, useRef, useEffect} from 'react';
import "../LogIn.css";
import NavigationBar from '../NavigationBar';

export function LogIn(){
    const userRef = useRef();
    const errRef = useRef();

    const [user, setUser] = useState('');
    const [pass, setPass] = useState('');
    const [errMsg, setErrMsg] = useState('');
    const [success, setSucess] = useState(false);

    useEffect(() => {
        userRef.current.focus();
    }, [])

    useEffect(() => {
        setErrMsg('');
    }, [user, pass])

    const handleSubmit = async (e) => {

    }

    return (
        <>
        <NavigationBar />
        <div className='login-container'>
        <section>
            <p ref={errRef} className={errMsg ? "errmsg" : "offscreen"} aria-live="assertive">{errMsg}</p>
                <form>
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