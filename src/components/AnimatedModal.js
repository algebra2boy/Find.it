import React from "react";
import Button from "@material-ui/core/Button";
import { makeStyles } from "@material-ui/core/styles";
import Modal from "@material-ui/core/Modal";
import Backdrop from "@material-ui/core/Backdrop";
import Fade from "@material-ui/core/Fade";
import "./AnimatedModal.css"

const useStyles = makeStyles((theme) => ({
    modal: {
        display: "flex",
        alignItems: "center",
        justifyContent: "center"
    },
    paper: {
        backgroundColor: theme.palette.background.paper,
        border: "3px solid #000",
        boxShadow: theme.shadows[5],
        padding: theme.spacing(2, 4, 3)
    }
}));

export default function AnimatedModal() {
    const classes = useStyles();
    const [open, setOpen] = React.useState(false);
    const handleOpen = () => {
        setOpen(true);
    };
    const handleClose = () => {
        setOpen(false);
    };
    return (
        <div>
            <Button variant="contained" color="secondary" onClick={handleOpen}>
                Open Animated Modal
            </Button>
            <Modal
                aria-labelledby="transition-modal-title"
                aria-describedby="transition-modal-description"
                className={classes.modal}
                open={open}
                onClose={handleClose}
                closeAfterTransition
                BackdropComponent={Backdrop}
                BackdropProps={{
                    timeout: 500
                }}
            >
                <Fade in={open}>
                    <div className={classes.paper}>
                        <h2>Posting an item</h2>
                        <form>
                            <label for="Name">Item Name:</label>
                            <input type="text" id="Name" name="Name" />
                            <label for="Location">Location:</label>
                            <input type="text" id="Location" name="Location" />
                            <label for="Description">Description:</label>
                            <input type="text" id="Description" name="Description" />
                            <label for="Date">Date:</label>
                            <input type="text" id="Date" name="Date" />
                            <input type="submit" value="Submit" />
                        </form>
                    </div>

                </Fade>
            </Modal>
        </div>
    );
}
