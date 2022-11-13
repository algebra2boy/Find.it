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
                      text = "This website is aimed to help people to search for their lost items, and for people who find lost items to help those items find their owners."
                      label = "Mission"
                      path = "/services"
                    />

                    <CardItem 
                      src = "images/hackumass.png"
                      text = " " //WHAT DO I ADD HERE?!?!?!
                      label = "Hackathon"
                      path = "/services"
                    />

                    <CardItem 
                      src = "images/lost_and_found.png"
                      text = "1. Make an account 2. Login 3. Search for your item, or post a lost one!"
                      label = "Steps"
                      path = "/services"
                    />

                    
                </ul>

                <ul className = "cards__items">
                    <CardItem //PULL THE FRESHEST DATA FROM THE DATABASE AND PLOP THE DATA HERE
                      src = "images/image-1.png" //IF WE DONT ALREADY, CREATE A PATH TO THE FILE (AND MAKE IT IF WE HAVE TO) THEN GIVE THE PATH
                      text = "Most recent lost item" 
                      label = "item1" //GET THE NAME OF THE ITEM
                      path = "/services"
                    />

                    <CardItem //SAME AS ABOVE ONLY WE TAKE THE OLDEST DATA
                      src = "images/image-1.png"
                      text = "Oldest lost item"
                      label = "item2"
                      path = "/services"
                    />
                </ul>
            </div>
        </div>
    </div>
  );
}

export default Cards;