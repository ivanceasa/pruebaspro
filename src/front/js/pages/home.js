import React, { useContext, useEffect } from "react";
import { Context } from "../store/appContext";
import "../../styles/home.scss";
import Topbar from "../component/topbar/Topbar";

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
			<Topbar />
			<h1>Esto es Home</h1>
		</>
	);
};
