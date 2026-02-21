terraform {
	required_providers {
		docker = {
			source = "kreuzwerker/docker"
			}
		}
	}

provider "docker" {}

resource "docker_network" "smart_monitor_net" {
	name = "smart-monitor-network"
}

resource "docker_image" "redis" {
	name = "redis:latest"
}

resource "docker_container" "redis" {
	name = "redis"
	image = docker_image.redis.image_id

	networks_advanced {
	name = docker_network.smart_monitor_net.name
	}
}

resource "docker_image" "monitor" {
	name = "smart-monitor:latest"
	build {
		context = "${path.module}/../app/monitor-app"
	}
}

resource "docker_container" "monitor" {
	name = "monitor-app"
	image = docker_image.monitor.image_id

	networks_advanced {
		name = docker_network.smart_monitor_net.name
	}

	depends_on = [docker_container.redis]
}

resource "docker_image" "action" {
	name = "smart-monitor-action:latest"

	build {
		context = "${path.module}/../app/action-app"
	}
}

resource "docker_container" "action" {
	name = "action-app"
	image = docker_image.action.image_id

	networks_advanced {
		name = docker_network.smart_monitor_net.name
	}

	env = [
	"TELEGRAM_BOT_TOKEN=${var.bot_token}",
	"TELEGRAM_CHAT_ID=${var.chat_id}",

	]

	depends_on = [docker_container.redis]
}

resource "docker_image" "aggregator" {
	name = "smart-monitor-aggregator:latest"

	build {
		context = "${path.module}/../app/aggregator"
	}
}

resource "docker_container" "aggregator" {
	name = "aggregator"
	image = docker_image.aggregator.image_id

	networks_advanced {
		name = docker_network.smart_monitor_net.name
	}
}
