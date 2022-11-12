import React from 'react';
import '../App.css';
import { Button } from './Button';
import './Background.css';

function Background() {
    return (
        <div className='hero-container'>
            <video src="./videos/CoolSky.mp4"
                autoPlay loop muted />
            <h1>Have YOU lost your item? </h1>
            <p>But you don't know where to find it</p>

            <div className='hero-btns'>
                {/* Customized Button we made in the button.js */}
                <Button
                    className='btns'
                    buttonStyle='btn--outline'
                    buttonSize='btn-large'
                >
                
                    FIND
                </Button>

                <Button
                    className='btns'
                    buttonStyle='btn--primary'
                    buttonSize='btn-large'
                >
                    GO <i className = 'farfa-play-circle'/>
                </Button>

            </div>

        </div>
    );
}

export default Background;