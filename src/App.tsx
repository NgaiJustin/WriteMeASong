import React from "react";
import "./App.css";
import "semantic-ui-css/semantic.min.css";
import Landing from "./Landing";
import Authenticated from "./Authenticated";
import ParticleBG from "./Particles";

function App() {
    return (
        <div className="App">
            <ParticleBG />
            <Authenticated>
                <Landing />
            </Authenticated>
        </div>
    );
}

export default App;
