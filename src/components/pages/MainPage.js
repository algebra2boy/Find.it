import React from 'react';
import { useLocation } from 'react-router-dom';
import NavigationBar from '../NavigationBar';
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
        {name:'Frozen yoghurt1', date: 159, time: 6.0, location: "home", description: "hello", },
        {name:'Frozen yoghurt2', date: 159, time: 6.0, location: "home", description: "hello"},
        {name:'Frozen yoghurt3', date: 159, time: 6.0, location: "home", description: "hello"},
        {name:'Frozen yoghurt4', date: 159, time: 6.0, location: "home", description: "hello"},
        {name:'Frozen yoghurt5', date: 159, time: 6.0, location: "home", description: "hello"},
        {name:'Frozen yoghurt6', date: 159, time: 6.0, location: "home", description: "hello"},
        {name:'Frozen yoghurt7', date: 159, time: 6.0, location: "home", description: "hello"},
        {name:'Frozen yoghurt8', date: 159, time: 6.0, location: "home", description: "hello"},
      ];
    return (
        <>
        <NavigationBar />
    <div className="table-container" style={{border: '1px solid black'}}>
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
    <div className="card-container">
        <ul className='card-list'>
        </ul>
    </div>
        </>
    )
}