import React from 'react';
import '../App.css';
import { Button } from './Button';
import './Background.css';

function Background() {
    return (
        <div className='background-container'>
            <video src="./videos/CoolSky.mp4"
                autoPlay loop muted />
            <h1>lost your item?</h1>
            <p>But you don't know where to find it?</p>

            <div className='background-btns'>
                {/* Customized Button we made in the button.js */}
                <Button
                    className='btns'
                    buttonStyle='button--fancy'
                    buttonSize='button--large'
                >
                
                    Sign
                </Button>

                <Button
                    className='btns'
                    buttonStyle='button--fancy'
                    buttonSize='button--large'
                >
                    Now
                </Button>

            </div>

        </div>
    );
}

export default Background;