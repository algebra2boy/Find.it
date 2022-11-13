import "../../App.css";
import React from 'react';
import Background from "../Background";
import NavigationBar from "../NavigationBar";
import Cards from "../Cards";

function Home () {
    return (
        <>
        <NavigationBar />
        <Background />
        <Cards />
        </>
    );
}

export default Home;