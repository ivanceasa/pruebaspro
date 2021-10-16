import React, { useContext, useEffect } from "react";
import { Context } from "../store/appContext";
import "../../styles/home.scss";

export const Home = () => {
	const { store, actions } = useContext(Context);
	useEffect(
		() => {
			if (store.token && store.token != "" && store.token != undefined) actions.getMessage();
		},
		[store.token]
	);

	return (
		<>
			<div className="card bg-dark text-white">
				<img
					src="https://p2.piqsels.com/preview/981/921/185/spain-santiago-path-road-path-thumbnail.jpg"
					className="img-fluid"
					alt="..."
				/>
				<div className="card-img-overlay text-center m-4">
					<h1 className="card-title font-weight-bold display-1 m-4">Bienvenido Peregrino!</h1>
					<p className="card-text display-4">
						Conoce las rutas y etapas, encuentra tu albergue y recibe consejos para el viaje
					</p>
					<p className="card-text display-4 m-4">
						Regístrate y comparte tu experiencia con otros peregrinos!
					</p>
				</div>
			</div>
			<div className="homeContainer" />
		</>
	);
};
