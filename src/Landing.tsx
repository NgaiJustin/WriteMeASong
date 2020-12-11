import React, { useState } from 'react';
import { Button, Header, Dropdown, Modal } from 'semantic-ui-react'
import InitialModal from './InitialModal';
import firebase from 'firebase';
import FirebaseAuth from 'react-firebaseui/FirebaseAuth';

const Landing = () => {
    const [genre, setGenre] = React.useState('');
    const [length, setLength] = React.useState(0);
    const [lyrics, setLyrics] = React.useState('');
    const handleGenreChange = (newValue: string) => {
        setGenre(newValue);
    }
    const handleLengthChange = (newValue: number) => {
        setLength(newValue);
    }
    const generateLyrics = async () => {
        try {
        const body = {
            "genre": genre,
            "lyrics": length
        }
        const response = await fetch('/gen-song', {
            method: 'POST',
            body: JSON.stringify(body)
        });
        const responseJson = await response.json()
        setLyrics(responseJson.lyrics)
        return response.json();
        } catch(e) {
            console.log(e);
        }
    }
    console.log(genre);
    return (
        <div>
        Genre is {genre==='' ? 'not selected yet' : genre}
        <br></br>
        Length is {length===0 ? 'not selected yet' : length}
        <br></br>
        <Button onClick={()=>generateLyrics()}>Generate Lyrics</Button>
        <br></br>
        {lyrics}
        <br></br>
        <Button onClick={()=>firebase.auth().signOut()}>Sign Out</Button>
            <InitialModal setGenre={handleGenreChange} setLength={handleLengthChange}/>
        </div>
    )
}

export default Landing