package clock.interfaces;

import java.util.Set;

import clock.enums.NodeType;
import clock.enums.Signal;


public abstract class TemporalFissure extends Node {

	private NodeType nodeType;

public TemporalFissure(NodeType nodeType) {
		super();
		this.nodeType = nodeType;
	}
	public TemporalFissure(NodeType nodeType, Set<Node> before, Set<Node> next) {
		super(before, next);
		this.nodeType = nodeType;
	}

	@Override
	public String toString() {
		return "TemporalFissure {" + this.nodeType + ", id:" + this.hashCode() + "}";
	}

	@Override
	public void addToNext(Node node) {
		throw new RuntimeException("Temporal Fissure can not have following nodes");
	}
	@Override
	public void removeFromNext(Node node) {
		throw new RuntimeException("Temporal Fissure can not have following nodes");
	}
}
