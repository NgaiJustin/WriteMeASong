import React, { useState } from 'react';
import { Button, Header, Dropdown, Modal } from 'semantic-ui-react'
import InitialModal from './InitialModal';
import firebase from 'firebase';
import FirebaseAuth from 'react-firebaseui/FirebaseAuth';

const Landing = () => {
    const [genre, setGenre] = React.useState('');
    const [length, setLength] = React.useState('');
    const [lyrics, setLyrics] = React.useState('');
    const handleGenreChange = (newValue: string) => {
        setGenre(newValue);
    }
    const handleLengthChange = (newValue: string) => {
        setLength(newValue);
    }
    const generateLyrics = async () => {
        try {
        let count = 0;
        switch(length) {
            case 'Less than 100 words': 
            count = Math.floor(Math.random()*101);
            break;
            case '100 - 200 words':
            count = Math.floor(Math.random()*101) + 100;
            break;
            case '200 - 300 words':
            count = Math.floor(Math.random()*101) + 200;
            break;
            case '300 - 400 words':
            count = Math.floor(Math.random()*101) + 300;
            break;
        }
        console.log('called');
        const body = {
            "genre": genre,
            "length": count
        }
        const response = await fetch('https://cors-anywhere.herokuapp.com/'+'http://127.0.0.1:8000/gen-song', {
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
        Length is {length==='' ? 'not selected yet' : length}
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