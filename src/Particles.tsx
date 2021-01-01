import Particles from "react-tsparticles";
import particleOptions from "./particles.json";

const ParticlesBackground = () => (
    <Particles id="tsparticles" options={particleOptions}></Particles>
);

export default ParticlesBackground;
