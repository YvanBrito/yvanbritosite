import React from "react";

import "./styles.css";

function DevItem(props) {
    const { dev } = props;
    return (
        <li key={dev._id} className="dev-item">
            <header>
                <img src={dev.avatar_url} alt={dev.name}></img>
                <div className="user-info">
                    <strong>{dev.name}</strong>
                    <span>{dev.techs.replace(/;/g, ', ')}</span>
                </div>
            </header>
            <p>{dev.bio}</p>
            <a href={`https://github.com/${dev.github_username}`}>
                Acessar perfil no github
            </a>
        </li>
    );
}

export default DevItem;
