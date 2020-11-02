package clock.interfaces;

import java.util.Set;

import clock.enums.NodeType;


public abstract class Gate extends Node {

	private NodeType nodeType;

	public Gate(NodeType nodeType) {
		super();
		this.nodeType = nodeType;
	}
	public Gate(NodeType nodeType, Set<Node> before, Set<Node> next) {
		super(before, next);
		this.nodeType = nodeType;
	}

	@Override
	public String toString() {
		return "Gate {" + this.nodeType + ", id:" + this.hashCode() + "}";
	}
}
