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
                    <CardItem //PULL THE FRESHEST DATA FROM THE DATABASE AND PLOP THE DATA HERE
                      src = "images/ring.jpeg" //IF WE DONT ALREADY, CREATE A PATH TO THE FILE (AND MAKE IT IF WE HAVE TO) THEN GIVE THE PATH
                      text = "A ring lost at the visitor parking at UMass on 11/13/2022" 
                      label = "item1" //GET THE NAME OF THE ITEM
                      path = "/"
                    />

                    <CardItem //SAME AS ABOVE ONLY WE TAKE THE OLDEST DATA
                      src = "images/lost_iphone.jpeg"
                      text = "Iphone 12 lost on the table at ILC 1st floor on 11/7/2022"
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