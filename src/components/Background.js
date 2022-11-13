import React from 'react';
import '../App.css';
import { Button } from './Button';
import './Background.css';

function Background() {
    return (
        <div className='background-container'>
            <video src="./videos/CoolSky.mp4"
                autoPlay loop muted />
            <h1>Lost something?</h1>
            <p>and can't find it?</p>

            <div className='background-btns'>
                {/* Customized Button we made in the button.js */}
                <Button
                    className='btns'
                    buttonStyle='button--fancy'
                    buttonSize='button--large'
                    link = "./sign-up"
                >
                
                    Sign up here!
                </Button>
{/* 
                <Button
                    className='btns'
                    buttonStyle='button--fancy'
                    buttonSize='button--large'
                >
                    Now
                </Button> */}

            </div>

        </div>
    );
}

export default Background;