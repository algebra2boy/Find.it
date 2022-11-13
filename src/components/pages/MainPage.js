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
import CardItem from '../CardItem';

export function MainPage() {
  const location = useLocation();

  const rows = [
    { name: 'Iphone', date: '04-22-2022', location: "home", description: "hello", firstName: 'Anan', phone: '27162327162', email: 'Anan@umass.edu' },
    { name: 'Mac', date: '04-16-2022', location: "home", description: "hello", firstName: 'Anan', phone: '27162327162', email: 'Anan@umass.edu'   },
    { name: 'Airpods', date: '04-27-2022', location: "home", description: "hello", firstName: 'Anan', phone: '27162327162', email: 'Anan@umass.edu'   },
    { name: 'Ipad', date: '04-10-2022', location: "home", description: "hello", firstName: 'Anan', phone: '27162327162', email: 'Anan@umass.edu'   },
    { name: 'water bottle', date: '04-12-2022', location: "home", description: "hello" , firstName: 'Anan', phone: '27162327162', email: 'Anan@umass.edu'  },
    { name: 'wallet', date: '04-19-2022', location: "home", description: "hello", firstName: 'Anan', phone: '27162327162', email: 'Anan@umass.edu'   },
    { name: 'backpack', date: '04-23-2022', location: "home", description: "hello", firstName: 'Anan', phone: '27162327162', email: 'Anan@umass.edu'   },
    { name: 'glasses', date: '04-24-2022', location: "home", description: "hello", firstName: 'Anan', phone: '27162327162', email: 'Anan@umass.edu'   },
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
                <Row key={row.name} row={row} status={false} />
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
