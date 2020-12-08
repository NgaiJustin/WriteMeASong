import React, { useState } from 'react';
import { Button, Header, Dropdown, Modal } from 'semantic-ui-react'
import InitialModal from './InitialModal';
import firebase from 'firebase';
import FirebaseAuth from 'react-firebaseui/FirebaseAuth';

const Landing = () => {
    const [genre, setGenre] = React.useState('');
    const [length, setLength] = React.useState(0);
    const handleGenreChange = (newValue: string) => {
        setGenre(newValue);
    }
    const handleLengthChange = (newValue: number) => {
        setLength(newValue);
    }
    console.log(genre);
    return (
        <div>
        Genre is {genre==='' ? 'not selected yet' : genre}
        <br></br>
        Length is {length===0 ? 'not selected yet' : length}
        <br></br>
        <button onClick={()=>firebase.auth().signOut()}>Sign Out</button>
            <InitialModal setGenre={handleGenreChange} setLength={handleLengthChange}/>
        </div>
    )
}

export default Landing