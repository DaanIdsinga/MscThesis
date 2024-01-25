# Assign Paved Areas

This workflow show how to add the determined paved areas to D-RR. The D-HYDRO modelbuilderscript of RoyalHaskoningDHV is used for this. D-RR is a part of this modelbuilderscript. The steps are given in this section to be able to reproduce the process and to add extra villages if needed.

## Step 1: Add Villages to D-RR

The villages are added at <I>Stap 6: Genereren RR model</I> in the modelbuilderscript. This block of code generates the D-RR schematization and new paved nodes can be added. The equation <I>drrmodel.paved.add\_paved()</I> is used for this. This equation needs the following parameters:

* 'id': Name of the RR paved node;
* 'area': Paved area of the RR paved node;
* 'surface_level': The surface level of the sewer overflow;
* 'street_storage': The amount of storage on the street;
* 'sewer_storage': The amount of storage in the sewer;
* 'pump_capacity': The capacity of the pump that pumps the water to the wastewater treatment plant
* 'meteo_area': The corresponding meteo area in the .BUI file. The precipitation of this area is the input of the paved node;
* 'px': X-coordinate of the paved node;
* 'py': Y-coordinate of the paved node;
* 'boundary_node': Corresponding boundary node, at which the excess water is discharged to the river. 

The villages are added with the lines of code below. The corresponding surface levels are retrieved from the available DEM. The coordinates of the nodes are randomly chosen, close to the boundary nodes. 

\begin{figure}[H]
    \centering
    \includegraphics[width=\linewidth]{Images/Add_paved_nodes.png}
    \caption{Python code for adding the new villages as paved nodes to D-RR.}
    \label{fig:nodes}
\end{figure}

Next, the boundary nodes are defined. These are nodes on the river, at which the excess water from the paved nodes enters the river. This is done by the equation \textit{drrmodel.external\_forcings.add\_boundary\_node()}. The needed parameters for this equation are:

\begin{itemize}
    \item 'id': The name of the boundary node, it should correspond with the 'boundary\_node' in \Cref{fig:nodes};
    \item 'px': X-coordinate of the boundary node;
    \item 'py': Y-coordinate of the boundary node.
\end{itemize}

\noindent The boundary nodes are created by the Python code in \Cref{fig:boundaries}. The boundary nodes should be on the river. It is chosen to use the coordinates of the HBV laterals as they are known. Kelmis is added at the HBV lateral 10.001\_B\_1, Montzen is added at 10.001\_B\_4, Gemmenich at 10.001\_B\_6, Plombieres at 10.001\_B\_5, and Hombourg at 13.001\_B\_3.

\begin{figure}[H]
    \centering
    \includegraphics[width=0.9\linewidth]{Images/Add_paved_boundaries.png}
    \caption{Python code for adding the boundary nodes, that are connected to the new paved nodes.}
    \label{fig:boundaries}
\end{figure}

\textbf{\subsubsection{Step 2: Run the modelbuilderscript}}

\noindent The second step is running the modelbuilderscript until \textbf{\textit{Stap 7.2: Wegschrijven FM model}}. This generates a folder containing the FM and RR folders. In the RR folder, a file is generated called \textit{PAVED.3B}. This file contains the parameters of each paved node. At \textbf{\textit{Stap 7.5: Wegschrijven RTCmodel}}, the RR folder is overwritten. To avoid undoing addition of the paved nodes, an extra step is needed.
\\\\
The \textit{PAVED.3B} file is overwritten with the \textit{PAVED.3B} file in the defined folder for RTC in \Cref{fig:rtcmap}. This file should be adjusted to contain the added villages. This is done by copying the lines that contain the new paved nodes from the \textit{PAVED.3B} in the generated folder, the last five lines in \Cref{fig:paved3b}, to the \textit{PAVED.3B} file in the RTC folder.

\begin{figure}[H]
    \centering
    \includegraphics[width=0.7\linewidth]{Images/rtcmap.png}
    \caption{An example of the location of the folder containing the \textit{PAVED.3B} file that overwrites \textit{Step 1}.}
    \label{fig:rtcmap}
\end{figure}

\newpage

\begin{figure}[H]
    \centering
    \includegraphics[width=\linewidth]{Images/paved3b.png}
    \caption{The created \textit{PAVED.3B} file containing the added paved nodes.}
    \label{fig:paved3b}
\end{figure}

\noindent When the file is adjusted, the last step \textbf{\textit{Stap 7.5: Wegschrijven RTCmodel}} can be run. This generates the correct and final version of the D-RR schematization.

\textbf{\subsubsection{Step 3: Copy D-RR to your D-HYDRO Model}}

\noindent The created D-RR schematization can be used in your D-HYDRO model. The RR folder can be copied to the folder that contains the D-HYDRO model. 

\textbf{\subsubsection{Step 4: Adjust PAVED.3B}}

\noindent The parameters of the paved nodes can be adjusted if needed. The defined storages can be adjusted, the pumpcapacity can be changed or the surface level can be modified. Another adjustable parameter is the runoff delay factor (ru in \Cref{fig:paved3b}). This factor delays the flow from the paved node to the river. The larger the distance between the paved node and the river, the smaller the runoff delay coefficient \citep{RR}.

\textbf{\subsubsection{Step 5: Adjust Geul\_v1.03\_feb\_2022\_new.ext}}

\noindent The file \textbf{\textit{Geul\_v1.03\_feb\_2022\_new.ext}} combines the external forcings or boundary conditions. This file connects the boundary condition type, the name of the boundary condition and the file containing the timeseries. Boundary conditions are for example water levels, laterals, and meteorological fields. The created paved nodes are new boundary conditions and have to be added to the external forcing file. This is done by the adding lines as in \Cref{fig:externalfor}, \citep{dhydro}. 

\begin{figure}[H]
    \centering
    \includegraphics[width=0.2\linewidth]{Images/external_forcing.png}
    \caption{Example of the added lines to the external forcing file for the added paved nodes.}
    \label{fig:externalfor}
\end{figure}

\newpage

\noindent The lateral discharge is defined by:

\begin{itemize}
    \item 'id': Id of the lateral discharge;
    \item 'name' Name of the lateral discharge;
    \item 'branchId': Branch on which the lateral discharge is located;
    \item 'chainage': Location on the branch of the point-lateral discharge [m];
    \item 'discharge': Prescribed discharge for the lateral.
\end{itemize}

\noindent In this case, the discharge is set to realtime, as it is computed at every timestep during the D-HYDRO run.

\textbf{\subsubsection{Step 6: Adjust dimr\_config.xml}}

\noindent The final step is adjusting the Deltares Integrated Model Runner (DIMR) file. The DIMR file couples the FM, RR, and RTC modules \citep{dhydro}. The boundary nodes need to be added in two ways. First, the lines under the heading \textit{<coupler name="flow\_to\_rr">} are added, as in \Cref{fig:flow2rr}. These lines pass the water level in the FM model to the paved nodes in D-RR. Next, the lines in \Cref{fig:rr2flow} are added under the heading \textit{<coupler name="rr\_to\_flow">}. With these lines, the generated discharge of the paved nodes in D-RR is passed to the FM module. The adjusted model is now ready for simulation.

\begin{figure}[H]
  \begin{subfigure}[b]{0.45\textwidth}
    \includegraphics[width=\textwidth]{Images/flowtorr.png}
    \caption{Passing water levels from FM to RR for the added paved nodes in the DIMR file.}
    \label{fig:flow2rr}
  \end{subfigure}
\hfill
  \begin{subfigure}[b]{0.45\textwidth}
    \includegraphics[width=\textwidth]{Images/rrtoflow.png}
    \caption{Passing water discharges from RR to FM for the added paved nodes in the DIMR file.}
    \label{fig:rr2flow}
  \end{subfigure}
  \caption{Adding the new paved nodes to the DIMR file.}
\end{figure}
