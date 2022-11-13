import React from 'react';
import CardItem from "./CardItem";
import "./Cards.css";

function Cards() {
  return (
    <div className = "cards">
        <h1>Check out what we are!</h1>
        <div className = "cards__container">
            <div className = "cards__wrapper">
                <ul className = "cards__items">
                    <CardItem 
                      src = "images/image-1.png"
                      text = "This website is aimed to help people to search for their lost items, and for people who find lost items to help those items find their owners."
                      label = "Mission"
                      path = "/"
                    />

                    <CardItem 
                      src = "images/hackumass.png"
                      text = "This is our submission to the UMASS Hackathon 2022!"
                      label = "Hackathon"
                      path = "/"
                    />

                    <CardItem 
                      src = "images/lost_and_found.png"
                      text = "1. Make an account 2. Login \n 3. Search for your item, or post a lost one!"
                      label = "Steps"
                      path = "/"
                    />

                    
                </ul>

                <ul className = "cards__items">
<<<<<<< HEAD
                    <CardItem 
                      src = "images/image-1.png"
                      text = "Hello, World, what is going on"
                      label = "item1"
=======
                    <CardItem //PULL THE FRESHEST DATA FROM THE DATABASE AND PLOP THE DATA HERE
                      src = "images/image-1.png" //IF WE DONT ALREADY, CREATE A PATH TO THE FILE (AND MAKE IT IF WE HAVE TO) THEN GIVE THE PATH
                      text = "Most recent lost item" 
                      label = "item1" //GET THE NAME OF THE ITEM
>>>>>>> main
                      path = "/"
                    />

                    <CardItem //SAME AS ABOVE ONLY WE TAKE THE OLDEST DATA
                      src = "images/image-1.png"
                      text = "Oldest lost item"
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