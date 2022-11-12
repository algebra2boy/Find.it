import React from 'react';
import './Button.css';
import { Link } from 'react-router-dom';

const STYLES = ['button--regular', 'buttom_fancy'];

const SIZES = ['button--medium', 'button-large'];

// make a class with customized properties
export const Button = (
    { children,
        type,
        onClick,
        buttonStyle,
        buttonSize
    }) => {
    // check if the "STYLES array" has the passed button style, if not, then default to the button-regular
    const checkButtonStyle = STYLES.includes(buttonStyle) ? buttonStyle : STYLES[0];
    // same as above, except it is for sizes
    const checkButtonSize = SIZES.includes(SIZES) ? SIZES: SIZES[0];

    return (
        <Link to='/sign-up' className = 'btn-mobile'>
            <button 
            // customize the button
            className = {`btn ${checkButtonStyle} ${checkButtonSize}`}
            onClick = {onClick}
            type = {type}>
            {children}
            </button>
        </Link>
    )
};