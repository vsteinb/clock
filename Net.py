package clock;

import java.util.HashSet;
import java.util.Set;

import clock.enums.LogLevel;
import clock.enums.Signal;

import clock.interfaces.Node;


//Singleton
public class Net {

	// Getters & Setters superfluous
	public Node startNode;		// access point to send signals to
	public LogLevel logLevel;


	private static Net instance = null;

	private Net() {
		this.startNode = null;
	}
	public static Net getInstance() {
		if (Net.instance != null) Net.instance = new Net();
		return Net.instance;
	}


	// could be used by nodes?
	public void print(Node node, String message) {	// Node is for debugging
		System.out.println(this.logLevel == LogLevel.DEBUG ? node.toString() + message : message);
	}

	// recursive walk through graph
	// breadth-first search
	// in case of loop structures: stop if previously visited was hit
	public void sendSignal(Signal signal) {
		if (this.startNode == null) return;

		Set<Object[]> initialLayer = new HashSet<>();
		Object[] entry = {signal, this.startNode};
		initialLayer.add(entry);

		this.sendSignal(initialLayer, new HashSet<>());
	}
	private void sendSignal(Set<Object[]> layer, Set<Node> history) {

		Set<Object[]> nextLayer = new HashSet<>();
		for (Object[] e : layer) {

			Node toNode = (Node)e[1];
			// detected loop, stop here
			if (history.contains(toNode)) continue;

			Signal signal = (Signal)e[0];
			// gate processes signal
			Signal processedSignal = toNode.processSignal(signal);
			history.add(toNode);

			// signal did not pass through, stop here
			if (processedSignal == null) continue;

			// add next nodes to new layer
			for (Node n : toNode.getNext()) {
				Object[] entry = {processedSignal, n};
				nextLayer.add(entry);
			}
		}
		// process underlying layers
		this.sendSignal(nextLayer, history);
	}


	private void addGate() {		// randomGate, random location (set next[] on new and existing nodes)
		// TODO
	}

	private void addTemporalFissue() {		// random fissue after random gate (not fissue, should not have nodes after)
		// TODO
	}
}
