import React from 'react';
import { useLocation } from 'react-router-dom';
import NavigationBarDashboard from '../NavigationBarDashboard'
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import Row from './Row';
import '../MainPage.css';

export function MainPage() {
  const location = useLocation();

  const rows = [
    { name: 'Frozen yoghurt1', date: 159, time: 6.0, location: "home", description: "hello", },
    { name: 'Frozen yoghurt2', date: 159, time: 6.0, location: "home", description: "hello" },
    { name: 'Frozen yoghurt3', date: 159, time: 6.0, location: "home", description: "hello" },
    { name: 'Frozen yoghurt4', date: 159, time: 6.0, location: "home", description: "hello" },
    { name: 'Frozen yoghurt5', date: 159, time: 6.0, location: "home", description: "hello" },
    { name: 'Frozen yoghurt6', date: 159, time: 6.0, location: "home", description: "hello" },
    { name: 'Frozen yoghurt7', date: 159, time: 6.0, location: "home", description: "hello" },
    { name: 'Frozen yoghurt8', date: 159, time: 6.0, location: "home", description: "hello" },
  ];
  return (
    <>
      <NavigationBarDashboard />
      <div className="table-container" style={{ border: '1px solid black' }}>
        <TableContainer component={Paper}>
          <Table aria-label="collapsible table">
            <TableHead>
              <TableRow>
                <TableCell />
                <TableCell>Item Name</TableCell>
                <TableCell align="right">Date</TableCell>
                <TableCell align="right">Location</TableCell>
                <TableCell align="right"></TableCell>
                <TableCell align="right"></TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {rows.map((row) => (
                <Row key={row.name} row={row} status={true} />
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      </div>
      <div className="cards">
        <h1>Check out the Found items!</h1>
        <div className="cards__container">
          <div className="cards__wrapper">
            <ul className="cards__items">
              <CardItem
                src="images/macbook.jpeg"
                text="Macbook Pro 14 inches was found on library 2nd floor"
                label="laptop"
              />

              <CardItem
                src="images/bottle.webp"
                text="Water Bottle was found near Downtown library!"
                label="bottle"
              />

              <CardItem
                src="images/key.jpeg"
                text="A room key was found at the Worcester Dinning Hall!"
                label="key"
              />


            </ul>

            <ul className="cards__items">
              <CardItem
                src="images/ring.jpeg"
                text="A ring found at the visitor parking at UMass just this morning"
                label="keyboard"
              />

              <CardItem
                src="images/lost_iphone.jpeg"
                text="Blue bike got found near University Health Service just today!"
                label="Bike"
              />
            </ul>
          </div>
        </div>
      </div>
    </>
  )
}

export default MainPage;
