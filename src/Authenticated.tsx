import React, { useState, useEffect } from 'react';
import 'firebase/auth';
import firebase from 'firebase';
import FirebaseAuth from 'react-firebaseui/FirebaseAuth';

const firebaseConfig = {
    apiKey: "AIzaSyBASg3NFLA6No6bmE8Rk5TRUrR_9adia_w",
    authDomain: "writemeasong-5b07c.firebaseapp.com",
    projectId: "writemeasong-5b07c",
    storageBucket: "writemeasong-5b07c.appspot.com",
    messagingSenderId: "1016292934711",
    appId: "1:1016292934711:web:27d0758e6e248bcd322bb2",
    measurementId: "G-1R48TXSB2L"
};

firebase.initializeApp(firebaseConfig);

type Props = {
  readonly children: React.ReactNode;
};

const Authenticated = ({ children }: Props) => {
  const [user, setUser] = useState<firebase.User | null>(null);

  const uiConfig = {
    signInFlow: 'popup',
    signInOptions: [firebase.auth.GoogleAuthProvider.PROVIDER_ID],
  };

  function onAuthStateChange() {
    return firebase.auth().onAuthStateChanged((user) => {
      setUser(user);
    });
  }

  useEffect(() => onAuthStateChange(), []);

  return (
    <div>
      {user && children}
      {!user && (
        <div>
        Welcome to Write Me a Song!
        <FirebaseAuth uiConfig={uiConfig} firebaseAuth={firebase.auth()} />
        </div>
      )}
    </div>
  );
};

export default Authenticated;