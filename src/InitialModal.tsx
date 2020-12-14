import React, { useState, Dispatch } from 'react';
import { Button, Header, Dropdown, Modal } from 'semantic-ui-react'

type props = {
    setGenre: Function,
    setLength: Function,
    generateLyrics: Function,
    setOpen: Function,
    open: boolean
}

const InitialModal = (props: props) => {
    const genreOptions = [
        {
            text: 'Pop',
            value: 'pop',
        },
        {
            text: 'Rock',
            value: 'rock'
        },
        {
            text: 'Rap',
            value: 'rap'
        },
        {
            text: 'Country',
            value: 'country'
        },
        {
            text: 'Xmas',
            value: 'xmas'
        }
    ]

    const lengthOptions = [
        {
            text: 'Less than 100 words',
            value: 'Less than 100 words'
        },
        {
            text: '100 - 200 words',
            value: '100 - 200 words'
        },
        {
            text: '200 - 300 words',
            value: '200 - 300 words'
        },
        {
            text: '300 - 400 words',
            value: '300 - 400 words'
        }   
    ]

    const handleGenerateLyrics = () => {
        props.generateLyrics();
        props.setOpen(false);
    }
    
    return (
        <div>
            <Modal 
                closeIcon
                open={props.open}
                onClose={() => props.setOpen(false)}
                onOpen={() => props.setOpen(true)}
                closeOnDimmerClick={false}
            >
            <Header icon='music' content='Choose your preferences!' />
                <Modal.Content>
                    Genre:
                    <Dropdown
                        placeholder='select genre'
                        fluid
                        selection
                        options = {genreOptions}
                        onChange = {(e, {value})=>{props.setGenre(value)}}
                    />
                    Length:
                    <Dropdown
                        placeholder='select length'
                        fluid
                        selection
                        options = {lengthOptions}
                        onChange = {(e, {value})=>{props.setLength(value)}}
                        style = {{marginBottom: '10px'}}
                    />
                    <Button style={{margin: 'auto', display:'block'}} onClick={()=>handleGenerateLyrics()}>Generate Lyrics</Button>
                </Modal.Content>
            </Modal>
        </div>
    )
}

export default InitialModal;