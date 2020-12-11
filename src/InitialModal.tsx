import React, { useState, Dispatch } from 'react';
import { Button, Header, Dropdown, Modal } from 'semantic-ui-react'

type props = {
    setGenre: Function,
    setLength: Function,
}

const InitialModal = (props: props) => {
    const [open, setOpen] = React.useState(true);
    const genreOptions = [
        {
            text: 'Pop',
            value: 'Pop',
        },
        {
            text: 'Rock',
            value: 'Rock'
        },
        {
            text: 'Rap',
            value: 'Rap'
        },
        {
            text: 'Country',
            value: 'Country'
        },
        {
            text: 'Xmas',
            value: 'Xmas'
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
    
    return (
        <div>
            <Modal 
                closeIcon
                open={open}
                onClose={() => setOpen(false)}
                onOpen={() => setOpen(true)}
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
                    />
                </Modal.Content>
            </Modal>
        </div>
    )
}

export default InitialModal;