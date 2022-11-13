import React, {useState, useRef, useEffect} from 'react';

import Box from '@mui/material/Box';
import Collapse from '@mui/material/Collapse';
import IconButton from '@mui/material/IconButton';
import TableCell from '@mui/material/TableCell';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Typography from '@mui/material/Typography';
import KeyboardArrowDownIcon from '@mui/icons-material/KeyboardArrowDown';
import Delete from '@mui/icons-material/Delete';
import Update from '@mui/icons-material/Update';
import Face from '@mui/icons-material/Face';
import KeyboardArrowUpIcon from '@mui/icons-material/KeyboardArrowUp';
import Button from 'react-bootstrap/Button';
import Modal from '@mui/material/Modal'
import Dialog from '@mui/material/Dialog'
import TextField from '@mui/material/TextField'
import DialogContent from '@mui/material/DialogContent'
import DialogActions from '@mui/material/DialogActions'
import DialogContentText from '@mui/material/DialogContentText'
import '../Row.css'

export function Row(props) {
    const { row, status } = props;
    const [open, setOpen] = React.useState(false);
    const [showProfile, setShowProfile] = useState(false);


    const updateHandler = () => {
        console.log()
    }

    const openShowProfile = () => setShowProfile(true);
    const closeShowProfile = () => setShowProfile(false);
    const style = {
        position: 'absolute',
        top: '50%',
        left: '50%',
        transform: 'translate(-50%, -50%)',
        width: 400,
        bgcolor: 'background.paper',
        border: '2px solid #000',
        boxShadow: 24,
        p: 4,
      };
    return (
        <>
        {!status ?
        <Modal
        open={showProfile}
        onClose={closeShowProfile}
        aria-labelledby="modal-modal-title"
        aria-describedby="modal-modal-description"
      >
        <Box sx={style}>
          <Typography id="modal-modal-title" variant="h6" component="h2">
            Name
          </Typography>
          <div>{row.firstName}</div>
          <Typography id="modal-modal-description" sx={{ mt: 2 }}>
            Contact Info
          </Typography>
          <div>{row.phone}</div>
          <div>{row.email}</div>
        </Box>
      </Modal>
      :
      <Dialog
        open={showProfile}
        onClose={closeShowProfile}
      >
        <DialogContent>
        <DialogContentText>
            Are you sure about deleting this?
        </DialogContentText>
        <DialogActions>
        <button className="buttons" onClick={updateHandler}>delete</button>
        <button className="buttons" onClick={closeShowProfile}>close</button>
        </DialogActions>
        </DialogContent>
      </Dialog>}
      <React.Fragment>
        <TableRow sx={{ '& > *': { borderBottom: 'unset' } }}>
          <TableCell>
            <IconButton
              aria-label="expand row"
              size="small"
              onClick={() => setOpen(!open)}
            >
              {open ? <KeyboardArrowUpIcon /> : <KeyboardArrowDownIcon />}
            </IconButton>
          </TableCell>
          <TableCell component="th" scope="row">
            {row.name}
          </TableCell>
          <TableCell align="right">{row.date}</TableCell>
          <TableCell align="right">{row.location}</TableCell>
          <TableCell align="right">{status ? <IconButton onClick={openShowProfile}><Delete/></IconButton>
          : <IconButton onClick={openShowProfile}><Face/></IconButton>}</TableCell>
        </TableRow>
        <TableRow>
          <TableCell style={{ paddingBottom: 0, paddingTop: 0 }} colSpan={6}>
            <Collapse in={open} timeout="auto" unmountOnExit>
              <Box sx={{ margin: 1 }}>
                <Typography variant="h6" gutterBottom component="div">
                  description
                </Typography>
                <div>{row.description}</div>
              </Box>
            </Collapse>
          </TableCell>
        </TableRow>
      </React.Fragment>
      </>
    );
  }

  export default Row;