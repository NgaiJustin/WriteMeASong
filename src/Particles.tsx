import Particles from "react-tsparticles";
import defaultOptions from "./particlesOptions/default.json";
import xmasOptions from "./particlesOptions/xmas.json";
import popOptions from "./particlesOptions/pop.json";
import rapOptions from "./particlesOptions/rap.json";
import rockOptions from "./particlesOptions/rock.json";
import countryOptions from "./particlesOptions/country.json";

type Props = { readonly genre: string };

const ParticlesBackground = ({ genre }: Props) => {
    let option: any = defaultOptions;
    switch (genre) {
        case "xmas":
            option = xmasOptions;
            break;
        case "pop":
            option = popOptions;
            break;
        case "rap":
            option = rapOptions;
            break;
        case "rock":
            option = rockOptions;
            break;
        case "country":
            option = countryOptions;
            break;
        default:
            option = defaultOptions;
            break;
    }
    return <Particles id="tsparticles" options={option}></Particles>;
};

export default ParticlesBackground;
