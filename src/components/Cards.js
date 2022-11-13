import React from 'react';
import CardItem from "./CardItem";
import "./Cards.css";

function Cards() {
  return (
    <div className = "cards">
        <h1>Check out who we are!</h1>
        <div className = "cards__container">
            <div className = "cards__wrapper">
                <ul className = "cards__items">
                    <CardItem 
                      src = "images/image-1.png"
                      text = "This website app is aimed to help people to find and search their lost items"
                      label = "Mission"
                      path = "/"
                    />

                    <CardItem 
                      src = "images/hackumass.png"
                      text = " 1. Make an account 2. Login 3."
                      label = "Hackathon"
                      path = "/"
                    />

                    <CardItem 
                      src = "images/lost_and_found.png"
                      text = "Hello, World, what is going on"
                      label = "Steps"
                      path = "/"
                    />

                    
                </ul>

                <ul className = "cards__items">
                    <CardItem 
                      src = "images/image-1.png"
                      text = "Hello, World, what is going on"
                      label = "item1"
                      path = "/"
                    />

                    <CardItem 
                      src = "images/image-1.png"
                      text = "Hello, World, what is going on"
                      label = "item2"
                      path = "/"
                    />
                </ul>
            </div>
        </div>
    </div>
  );
}

export default Cards;