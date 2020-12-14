import React, { useState } from 'react';
import { Button, Header, Dropdown, Modal } from 'semantic-ui-react'
import InitialModal from './InitialModal';
import firebase from 'firebase';
import FirebaseAuth from 'react-firebaseui/FirebaseAuth';
import background from './images/background.png';

const Landing = () => {
    const [genre, setGenre] = React.useState('');
    const [length, setLength] = React.useState('');
    const [lyrics, setLyrics] = React.useState('');
    const [open, setOpen] = React.useState(true);
    const handleGenreChange = (newValue: string) => {
        setGenre(newValue);
    }
    const handleLengthChange = (newValue: string) => {
        setLength(newValue);
    }
    const handleOpen = (newValue: boolean) => {
        setOpen(newValue);
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
        const body = {
            "genre": genre,
            "length": count
        }
        const response = await fetch('/gen-song', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(body)
        });
        const responseJson = await response.json()
        setLyrics(responseJson.lyrics)
        return responseJson;
        } catch(e) {
            console.log(e);
        }
    }
    return (
        <div style={{backgroundImage: `url(${background})`, height: '700px', color: 'white'}} className='container'>
            <InitialModal setGenre={handleGenreChange} setLength={handleLengthChange} generateLyrics={generateLyrics} setOpen={handleOpen} open={open}/>
        <div style={{fontSize: 'large', padding: '20px'}}>
        Genre is {genre==='' ? 'not selected yet' : genre} <br></br>
        Length is {length==='' ? 'not selected yet' : length}
        </div>
        <div style={{fontSize: '17px', textDecoration: 'underline', padding: '10px'}}>
        Generated Lyrics:
        </div>
        <div style={{margin: 'auto', width: '50%'}}>
        {lyrics}
        </div>
        <Button style={{margin:'10px'}} onClick={()=>{handleOpen(true)}}>Run it back</Button>
        <Button style={{margin:'10px'}} onClick={()=>firebase.auth().signOut()}>Sign Out</Button>
        </div>
    )
}

export default Landing